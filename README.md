<h1 align="center">FlappyBird-AI</h1>

<p align="center">
  <b>A Reinforcement Learning based Flappy Bird agent trained using Proximal Policy Optimization (PPO).</b>
</p>

---

## Overview

FlappyBird-AI is a Reinforcement Learning project where an autonomous agent learns to play Flappy Bird using **Proximal Policy Optimization (PPO)**.

The objective was to train an agent capable of consistently outperforming a human player while maintaining stable learning. After experimenting with different RL algorithms, PPO was selected over DQN due to its significantly more stable training behavior.

The trained PPO agent consistently achieves **60–150 points**, whereas my average human score is around **15**, making the agent approximately **4× better on average** and capable of reaching **up to 10× higher scores**.

---

## Results

| Player | Average Score |
|---------|--------------:|
| Human (Me) | ~15 |
| PPO Agent | 60–150 |
| Transformer-based DQN (Benchmark) | ~200 |

The Transformer-based DQN model was **not trained by me** and was used solely as a benchmark for comparison.

---

## Why PPO instead of DQN?

Initially, I experimented with **Deep Q-Networks (DQN)**. However, during training I observed:

- Unstable convergence
- Large fluctuations in performance
- Difficulty achieving consistent policies
- Poor sample efficiency for this environment

To overcome these issues, I switched to **Proximal Policy Optimization (PPO)**.

PPO provided:

- Stable policy updates
- Faster convergence
- More reliable training
- Consistent gameplay performance

Although the benchmark Transformer-based DQN agent can achieve higher scores (~200), PPO produced a robust and reproducible agent with considerably more stable learning.

---

## Tech Stack

- Python
- Stable-Baselines3
- Gymnasium
- Matplotlib (training visualization)

---

## Key Features

- Reinforcement Learning based Flappy Bird agent
- PPO policy optimization
- Stable and reproducible training pipeline
- Performance benchmarking against a Transformer-based DQN agent
- Human vs AI performance comparison

---

## Project Highlights

- Trained an autonomous Flappy Bird agent using **Proximal Policy Optimization (PPO)**.
- Achieved **4× higher average performance** than a human player.
- Reached **60–150 scores** consistently during evaluation.
- Benchmarked against a **Transformer-based DQN** implementation.
- Switched from **DQN to PPO** after identifying instability in DQN training.

---

## Future Improvements

- Hyperparameter optimization
- Reward shaping experiments
- Frame stacking and improved state representation
- Curriculum learning
- Experiment with recurrent policies (LSTM PPO)
- Multi-environment parallel training

---

## Acknowledgements

The Transformer-based DQN implementation used for benchmarking was developed by another author and served only as a performance reference.
