#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *


class TestSuite:

    def test(self):

        # EVEX.128.66.0F3A.W0 66 /r ib
        # vfpclassps xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst, imm8

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}662011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x66)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfpclassps ')
        assert_equal(myDisasm.instr.repr, 'vfpclassps xmm4, xmm0, xmmword ptr [rax], 11h')

        # EVEX.256.66.0F3A.W0 66 /r ib
        # vfpclassps ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst, imm8

        myEVEX = EVEX('EVEX.256.66.0F3A.W0')
        Buffer = '{}662011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x66)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfpclassps ')
        assert_equal(myDisasm.instr.repr, 'vfpclassps ymm4, ymm0, ymmword ptr [rax], 11h')

        # EVEX.512.66.0F3A.W0 66 /r ib
        # vfpclassps zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst{sae}, imm8

        myEVEX = EVEX('EVEX.512.66.0F3A.W0')
        Buffer = '{}662011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x66)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfpclassps ')
        assert_equal(myDisasm.instr.repr, 'vfpclassps zmm4, zmm0, zmmword ptr [rax], 11h')

        # EVEX.128.66.0F3A.W1 66 /r ib
        # vfpclasspd xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst, imm8

        myEVEX = EVEX('EVEX.128.66.0F3A.W1')
        Buffer = '{}662011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x66)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfpclasspd ')
        assert_equal(myDisasm.instr.repr, 'vfpclasspd xmm4, xmm0, xmmword ptr [rax], 11h')

        # EVEX.256.66.0F3A.W1 66 /r ib
        # vfpclasspd ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst, imm8

        myEVEX = EVEX('EVEX.256.66.0F3A.W1')
        Buffer = '{}662011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x66)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfpclasspd ')
        assert_equal(myDisasm.instr.repr, 'vfpclasspd ymm4, ymm0, ymmword ptr [rax], 11h')

        # EVEX.512.66.0F3A.W1 66 /r ib
        # vfpclasspd zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst{sae}, imm8

        myEVEX = EVEX('EVEX.512.66.0F3A.W1')
        Buffer = '{}662011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x66)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfpclasspd ')
        assert_equal(myDisasm.instr.repr, 'vfpclasspd zmm4, zmm0, zmmword ptr [rax], 11h')