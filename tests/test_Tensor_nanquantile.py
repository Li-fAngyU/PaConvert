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

obj = APIBase("torch.Tensor.nanquantile")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([1.02, 2.21, 3.333, 30], dtype=torch.float64)
        result = x.nanquantile(0.5)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([float('nan'), 2.21, 3.333, 30], dtype=torch.float64)
        result = x.nanquantile(0.6, dim=0)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([float('nan'), 1.02, 2.21, 3.333,30, float('nan')], dtype=torch.float64)
        result = x.nanquantile(q=0.3, dim=-1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[float('nan'), 1.02, 2.21, 3.333,30, float('nan')]], dtype=torch.float64)
        result = x.nanquantile(q=0.3, dim=1, keepdim=True)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[float('nan'), 1.02, 2.21, 3.333,30, float('nan')]], dtype=torch.float64)
        result = x.nanquantile(q=0.3, dim=1, keepdim=False)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[0]], dtype=torch.float64)
        result = x.nanquantile(0.3, 1, True)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[0]], dtype=torch.float64)
        result = x.nanquantile(q=0.3, dim=1, keepdim=True, interpolation='higher')
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="Paddle not support this parameter",
    )