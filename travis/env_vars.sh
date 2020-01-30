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

export BEZIER_WHEEL=True
if [[ -n "${IS_OSX}" ]]; then
    export BEZIER_INSTALL_PREFIX="${TRAVIS_BUILD_DIR}/bezier/.nox/libbezier-release/usr"
else
    export BEZIER_INSTALL_PREFIX="/io/bezier/.nox/libbezier-release/usr"
fi
export TARGET_NATIVE_ARCH=OFF
export NOX_INSTALL_CMAKE=True
