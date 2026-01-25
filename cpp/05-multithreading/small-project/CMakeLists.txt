
cmake_minimum_required(VERSION 3.24)

#
#
#

add_executable(multi-threading
  ./src/main.cpp
  ./src/utilities/DeterministicRng.cpp
  ./src/tasks-runner/AbstractTasksScheduler.cpp
  ./src/tasks-runner/internals/ConcreteTasksScheduler.cpp
  ./src/tasks-runner/internals/ThreadSynchronizer.cpp
  ./src/tasks-runner/internals/TaskRunner.cpp
)

target_include_directories(multi-threading PRIVATE ./src/)

target_link_libraries(multi-threading PRIVATE -lpthread)

#
#
#
