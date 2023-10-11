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

obj = APIBase("torch.Tensor.view")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.arange(4.)
        result = a.view(2, 2)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.arange(4.)
        result = a.view((2, 2))
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.arange(9.)
        result = a.view([3, 3])
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.arange(9)
        shape = (3, 3)
        result = a.view(shape)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.arange(9)
        shape = (3, 3)
        result = a.view(*shape)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.arange(4.)
        k = 2
        result = a.view((k, k))
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.arange(2.)
        k = 2
        result = a.view(k)
        """
    )
    obj.run(pytorch_code, ["result"])


# # 因为当前paddle.view 不支持没有 shape 的 tensor，所以该案例无法正常运行
# def test_case_9():
#     pytorch_code = textwrap.dedent(
#         """
#         import torch
#         a = torch.tensor(1.)
#         result = a.view(1)
#         """
#     )
#     obj.run(pytorch_code, ["result"])


def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.arange(6.)
        result = a.view((2, 3))
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_9():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.arange(6.)
        result = a.view(torch.int32)
        """
    )
    obj.run(pytorch_code, ["result"])
