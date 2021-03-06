import torch
import torch.nn as nn
import numpy as np


class Population:
    def __init__(self, popSize, inputSize):
        self.agent = Agent(inputSize)
        self.mutatedAgents = [self.agent.mutate() for _ in range(popSize)]
        self.points = np.zeros(popSize)

        self.timestep = 0


    def act(self, states, deads):
        actions = []
        for mutated, state, dead in zip(self.mutatedAgents, states, deads):
            if not dead:
                actions.append(mutated[0](state) > 0.5)
            else:
                actions.append(False)
        return actions

    def evolve(self):
        self.points = (self.points - np.mean(self.points)) / (np.std(self.points) + 1e-10)
        noisySteps = [mutated[1] for mutated in self.mutatedAgents]
        self.agent.evolve(self.points, noisySteps)

        self.mutatedAgents = [self.agent.mutate() for _ in range(len(self.mutatedAgents))]
        self.points *= 0

        if self.timestep % 5 == 0:
            self.agent.save("policy")
        self.timestep += 1

    def store(self, points):
        self.points += points

    def load(self, name):
        self.agent.load(name)
        self.mutatedAgents = [self.agent.mutate() for _ in range(len(self.mutatedAgents))]


class Agent:
    def __init__(self, inputSize, sigma=0.015, alpha=0.0003):
        self.inputSize = inputSize
        self.policy = Policy(inputSize)
        self.sigma = sigma
        self.alpha = alpha

        for name, param in self.policy.named_parameters():
            if name == "fc2.weight":
                param.data = torch.randn(param.data.shape) * 0.00001
            elif name == "fc2.bias":
                param.data = torch.zeros(param.data.shape)

    def act(self, state):
        return [self.policy(state) > 0.5]

    def mutate(self):
        mutatedPolicy = Policy(self.inputSize)
        noise = []
        for origParam, mutatedParam in zip(self.policy.parameters(), mutatedPolicy.parameters()):
            paramNoise = torch.randn(origParam.data.shape)
            mutatedParam.data = origParam.data + self.sigma * paramNoise
            noise.append(paramNoise)

        return mutatedPolicy, noise

    def evolve(self, points, noisySteps):
        for score, noise in zip(points, noisySteps):
            for param, paramNoise in zip(self.policy.parameters(), noise):
                param.data += self.alpha / (len(points)*self.sigma) * paramNoise * score

    def save(self, name):
        torch.save(self.policy.state_dict(), name + ".pt")

    def load(self, name):
        self.policy.load_state_dict(torch.load(name + ".pt"))


class Policy(nn.Module):
    def __init__(self, inputSize):
        super(Policy, self).__init__()

        self.fc1 = nn.Linear(inputSize, 32)
        self.activation = nn.ReLU()
        self.fc2 = nn.Linear(32, 1)
        self.sigmoid = nn.Sigmoid()

        for name, param in self.named_parameters():
            param.requires_grad_(False)


    def forward(self, x):
        x = self.fc1(x)
        x = self.activation(x)
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x
