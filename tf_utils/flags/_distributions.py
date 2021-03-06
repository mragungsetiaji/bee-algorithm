"""Flags related to distributed execution."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import flags
import tensorflow as tf

from tf_utils.flags._conventions import help_wrap


def define_distribution(worker_hosts=True, task_index=True):
  """Register distributed execution flags.
  Args:
    worker_hosts: Create a flag for specifying comma-separated list of workers.
    task_index: Create a flag for specifying index of task.
  Returns:
    A list of flags for core.py to marks as key flags.
  """
  key_flags = []

  if worker_hosts:
    flags.DEFINE_string(
        name='worker_hosts', default=None,
        help=help_wrap(
            'Comma-separated list of worker ip:port pairs for running '
            'multi-worker models with DistributionStrategy.  The user would '
            'start the program on each host with identical value for this '
            'flag.'))

  if task_index:
    flags.DEFINE_integer(
        name='task_index', default=-1,
        help=help_wrap('If multi-worker training, the task_index of this '
                       'worker.'))

  return key_flags