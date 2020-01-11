# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Define custom utilities
# Test for OSX with [ -n "$IS_OSX" ]

function pip_opts {
    # Extra options for pip
    echo "-v"
}

function run_tests {
    echo "Executing run_tests ..."
    echo "python --version:"
    python --version
    if [[ -n "${IS_OSX}" ]]; then
        BEZIER_TESTS=${TRAVIS_BUILD_DIR}/bezier/tests
    else
        # I.e. running on a Docker container
        BEZIER_TESTS=/io/bezier/tests
    fi
    pytest ${BEZIER_TESTS}
}
