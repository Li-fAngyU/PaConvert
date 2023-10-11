# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import textwrap

from apibase import APIBase

obj = APIBase("torch.fft.ihfftn")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        t = torch.arange(20).reshape((4, 5)).type(torch.float64)
        result = torch.fft.ihfftn(t, s=(2, 5))
        """
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5, atol=1.0e-8)


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        t = torch.arange(20).reshape((4, 5)).type(torch.float64)
        result = torch.fft.ihfftn(t)
        """
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5, atol=1.0e-8)


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        t = torch.arange(20).reshape((4, 5)).type(torch.float64)
        result = torch.fft.ihfftn(t, dim=(0, 1))
        """
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5, atol=1.0e-8)


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        t = torch.arange(20).reshape((4, 5)).type(torch.float64)
        result = torch.fft.ihfftn(t, s=(2, 5), norm='ortho')
        """
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5, atol=1.0e-8)


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        t = torch.arange(20).reshape((4, 5)).type(torch.float64)
        result = torch.fft.ihfftn(t, s=(2, 5), norm='forward')
        """
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5, atol=1.0e-8)


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        t = torch.arange(20).reshape((4, 5)).type(torch.float64)
        result = torch.fft.ihfftn(t, s=(2, 5), norm='backward')
        """
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5, atol=1.0e-8)