import flappy_bird_gymnasium
import gymnasium

from stable_baselines3 import DQN, PPO

env = gymnasium.make(
    "FlappyBird-v0",
    render_mode="human",
    use_lidar=True
)

model = PPO.load("models/flappy_ppo") # Hard Coded here, change this line if you want to use dqn 

obs, _ = env.reset()

done = False
total_reward = 0

while not done:

    action, _ = model.predict(
        obs,
        deterministic=True
    )

    obs, reward, terminated, truncated, info = env.step(action)

    done = terminated or truncated

    total_reward += reward

print("Final Reward:", total_reward)

env.close()
