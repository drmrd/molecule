#  Copyright (c) 2015-2017 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import pytest


@pytest.fixture
def patched_ansible_playbook(mocker):
    m = mocker.patch('molecule.provisioner.ansible_playbook.AnsiblePlaybook')
    m.return_value.execute.return_value = b'patched-ansible-playbook-stdout'

    return m


@pytest.fixture
def patched_write_inventory(mocker):
    return mocker.patch(
        'molecule.provisioner.ansible.Ansible._write_inventory')


@pytest.fixture
def patched_remove_vars(mocker):
    return mocker.patch('molecule.provisioner.ansible.Ansible._remove_vars')


@pytest.fixture
def patched_link_or_update_vars(mocker):
    return mocker.patch(
        'molecule.provisioner.ansible.Ansible._link_or_update_vars')
