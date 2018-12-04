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

"""Check that speedups were built."""

from __future__ import print_function

import bezier


def main():
    print("bezier._HAS_SPEEDUP: {}".format(bezier._HAS_SPEEDUP))
    speedup_module = getattr(bezier, "_speedup", None)
    print("bezier._speedup: {}".format(speedup_module))
    assert bezier._HAS_SPEEDUP


if __name__ == "__main__":
    main()
