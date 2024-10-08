# Copyright 2024 xiexianbin.cn
# All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#        http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import os

from aigc2md import exception


CURRENT_PATH = os.getcwd()

# open-webui
OPENWEBUI_BASE_URL = os.environ.get('OPENWEBUI_BASE_URL', 'https://ai.80.xyz/api/v1')
OPENWEBUI_JWT = os.environ.get(
  'OPENWEBUI_JWT',
  os.environ.get('OPEN_WEBUI_JWT', None))
if OPENWEBUI_JWT in ('', None):
    raise exception.UnKnownOpenWebUIJWT('please set open webui JWT by: export OPENWEBUI_JWT="<JWT 令牌>"')

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

DEFAULT_CATEGORIES = os.environ.get('DEFAULT_CATEGORIES', 'ansible,apm,blockchain,carbon,ceph,cicd,cloud,cloud-native,dns,docker,ebpf,git,golang,hardware,hpc,iot,java,kubernetes,linux,lua,mac,mongodb,monitor,network,nginx,nodejs,openssl,openstack,openvswitch,program,python,react,rust,sdn,security,software,ubuntu,ai')

DEFAULT_CATEGORIES_LIST = DEFAULT_CATEGORIES.split(',')
