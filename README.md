# Evolution Strategies with Flappy Bird

---

An implementation of [Evolution Strategies (ES)](https://arxiv.org/pdf/1703.03864.pdf), an alternative method to 
reinforcement learning, tested on the simple game of Flappy Bird. Reinforcement learning generally calculates 
probabilities for actions and changes the weights of a neural network based on a gradient. On the other hand, ES adds 
noise to the original network's weight parameters, creating a whole "generation" of "mutated" networks, and moves the 
weights in the direction of the average of each mutated network's added noise, weighted based on how well they perform. 
This estimates the gradient of the expected reward of the original network, without the use of backpropagation, which 
can reduce the time to train significantly if parallelized. 

ES also makes visualizing the training process quite fun.

## How to Use
Run `userPlay.py` to play by yourself and/or others, by changing the numBirds variable to however many players. Player 1
jumps by pressing A, player 2 presses B, etc.

Run `view.py` to view the current policy play flappy bird

Run `evolution.py` to train the policy, saving it at `policy.pt`. Changing the render variable to False makes it so that 
the screen isn't shown when training, which speeds up the process, and changing the loadPrevPolicy variable to True 
loads `policy.pt` to the network at the start of the training.