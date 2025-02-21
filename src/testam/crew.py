from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Testam():
	"""Testam crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	
	@agent
	def campus_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['campus_manager'],
			verbose=True
		)
	
	@agent
	def housing_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['housing_manager'],
			verbose=True
		)

	@task
	def assign_dormitory(self) -> Task:
		return Task(
			config=self.tasks_config['assign_dormitory'],
			agent=self.campus_manager(),
		)
	
	@task
	def assign_students(self) -> Task:
		return Task(
			config=self.tasks_config['assign_students'],
			agent=self.housing_manager(),
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Students crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)