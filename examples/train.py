#!/usr/bin/env python

# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import gymnasium as gym
import gym_carla
import carla
from stable_baselines3 import A2C
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor

def main():
  # parameters for the gym_carla environment
  params = {
    'number_of_vehicles': 0,
    'number_of_walkers': 0,
    'display_size': 256,  # screen size of bird-eye render
    'max_past_step': 1,  # the number of past steps to draw
    'dt': 0.1,  # time interval between two frames
    'discrete': False,  # whether to use discrete control space
    'discrete_acc': [-2.0, 0.0, 2.0],  # discrete value of accelerations
    'discrete_steer': [-0.2, 0.0, 0.2],  # discrete value of steering angles
    'continuous_accel_range': [-2.0, 2.0],  # continuous acceleration range
    'continuous_steer_range': [-0.3, 0.3],  # continuous steering angle range
    'ego_vehicle_filter': 'vehicle.lincoln*',  # filter for defining ego vehicle
    'port': 2000,  # connection port
    'town': 'Town10HD_Opt',  # which town to simulate
    'task_mode': 'random',  # mode of the task, [random, roundabout (only for Town03)]
    'max_time_episode': 120,  # maximum timesteps per episode
    'max_waypt': 20,  # maximum number of waypoints
    'obs_range': 32,  # observation range (meter)
    'lidar_bin': 0.125,  # bin size of lidar sensor (meter)
    'd_behind': 12,  # distance behind the ego vehicle (meter)
    'out_lane_thres': 2.0,  # threshold for out of lane
    'desired_speed': 2,  # desired speed (m/s)
    'max_ego_spawn_times': 100,  # maximum times to spawn ego vehicle
    'display_route': True,  # whether to render the desired route
    'pixor_size': 64,  # size of the pixor labels
    'pixor': False,  # whether to output PIXOR observation
  }

  # Set gym-carla environment
  env = gym.make('carla-v0', params=params)
  #vec_env = make_vec_env("carla-v0", n_envs=4, env_kwargs=params)
  check_env(env, warn=True)
  #check_env(vec_env, warn=True)

  """
  register(
    id='carla-v0',
    entry_point='CarlaEnv',
    max_episode_steps=100,
  )
  """
  
  # which RL algorithm to use
  model = A2C("MultiInputPolicy", env, learning_rate=0.003, ent_coef=0.2, gamma=0.3, n_steps=3, verbose=1, tensorboard_log="./tensorboard_test/")
  # train the agent
  model.learn(total_timesteps=20000, tb_log_name="20")
  # specify file name for saving agent
  model_name = "20"
  # save the agent to a file
  model.save(model_name)

  times_reset = 0

  '''
  while times_reset < 10:
    action = [2.0, 0.0]
    obs,r,done,info = env.step(action)

    if done:
      obs = env.reset()
      times_reset += 1
      print("times reset = " + str(times_reset))
  '''


if __name__ == '__main__':
  main()