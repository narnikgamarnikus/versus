#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A versus.taskapp beat -l INFO
