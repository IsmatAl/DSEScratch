from antlr4 import *
from .APPLexer import APPLexer
from .APPListener import APPListener
from .APPParser import APPParser
from jinja2 import Template
import re
from .blockToPython import scratchToPython


class ProjectJsonParser:

    def __init__(self):
        self.printPythonCodeListener = self.PrintPythonCodeListener(self)
        self.blocks = {}
        self.varCodeToName = {}
        self.inputType = ''
        self.fieldType = ''
        self.rootNodes = []
        self.funcAttrs = []

# convert string representation of boolean values to boolean type

    def toBool(self, str):
        if str == "true":
            return True
        elif str == "false":
            return False
        else:
            raise ValueError(
                "incorrect representation of booleaan value: " + str)

    class Block:
        def __init__(self, outer):

            self.outer = outer

        # String
        identifier = ''
        opcode = ''
        next = ''
        parent = ''

        # Block
        nextBlk = None
        parentBlk = None

        # Lists
        substacks = []
        inputList = []

        # maps
        fields = {}

        # boolean
        topLevel = False

        def __init__(self, identifier, opcode, next, parent, inputList, fields, substacks, topLevel):
            self.identifier = identifier
            self.opcode = opcode
            self.next = next
            self.parent = parent
            self.inputList = inputList
            self.fields = fields
            self.substacks = substacks
            self.topLevel = topLevel

        def isTopLevel(self):
            return self.topLevel

        def getOpcode(self):
            return self.opcode

        def setNextBlk(self, nextBlk):
            self.nextBlk = nextBlk

        def setParentBlk(self, parentBlk):
            self.parentBlk = parentBlk

        def hasNext(self):
            return self.next != "null"

        def hasParent(self):
            return self.parent != None

        def getIdentifier(self):
            return self.identifier

        def getNextBlk(self):
            return self.nextBlk

        def getParentBlk(self):
            return self.parentBlk

        def getNext(self):
            return self.next

        def getParent(self):
            return self.parent

        def getInputList(self):
            return self.inputList

        def getSubstacks(self):
            return self.substacks

        def getFields(self):
            return self.fields

    class PrintPythonCodeListener(APPListener):

        def __init__(self, outer):

            self.outer = outer

        identifier = ''
        opcode = ''
        next = ''
        parent = ''
        substacks = []
        topLevel = False
        fields = {}
        inputList = []

        def enterVariablePair(self, ctx: APPParser.VariablePairContext):
            varName = ctx.STRING().getText().strip('"')
            varIdentifier = ctx.value(0).getText().strip('"')
            self.outer.varCodeToName[varIdentifier] = varName
            pass

        # Enter a parse tree produced by APPParser#BlockIdentifier.
        def enterBlockIdentifier(self, ctx: APPParser.BlockIdentifierContext):
            self.identifier = ctx.STRING().getText().strip('"')
            pass

        # Enter a parse tree produced by APPParser#OpCodeOfBlk.
        def enterOpCodeOfBlk(self, ctx: APPParser.OpCodeOfBlkContext):
            self.opcode = ctx.op_code().getText().strip('"')
            pass

        # Enter a parse tree produced by APPParser#NextBlk.
        def enterNextBlk(self, ctx: APPParser.NextBlkContext):
            self.next = ctx.value().getText().strip('"')
            pass

        # Enter a parse tree produced by APPParser#ParentBlk.
        def enterParentBlk(self, ctx: APPParser.ParentBlkContext):
            self.parent = ctx.value().getText().strip('"')
            pass

        # Enter a parse tree produced by APPParser#inputVals.
        def enterInputVals(self, ctx: APPParser.InputValsContext):
            self.outer.inputType = ctx.input_type().getText().strip('"')
            # print(self.inputType)
            pass

        # Enter a parse tree produced by APPParser#InputOfBlk.
        def enterInputOfBlk(self, ctx: APPParser.InputOfBlkContext):
            self.substacks = []
            self.inputList = []
            pass

        # Enter a parse tree produced by APPParser#LiteralInput.
        def enterLiteralInput(self, ctx: APPParser.LiteralInputContext):
            input = ctx.value().getText()
            if not self.outer.inputType.startswith("SECS"):
                self.inputList.append(input)
            pass

        # Enter a parse tree produced by APPParser#ValInput.
        def enterValInput(self, ctx: APPParser.ValInputContext):
            input = ctx.value().getText().strip('"')
            self.inputList.append(input)
            pass

        # Enter a parse tree produced by APPParser#InstrucInput.
        def enterInstrucInput(self, ctx: APPParser.InstrucInputContext):
            input = ctx.value().getText().strip('"')
            if self.outer.inputType.startswith("SUBSTACK"):
                self.substacks.append(input)
            else:
                self.inputList.append(input)
            pass

        # Enter a parse tree produced by APPParser#FieldsOfBlk.
        def enterFieldsOfBlk(self, ctx: APPParser.FieldsOfBlkContext):
            self.fields = {}
            pass

        # Enter a parse tree produced by APPParser#fieldPair.
        def enterFieldPair(self, ctx: APPParser.FieldPairContext):
            self.outer.fieldType = ctx.field_type().getText().strip('"')
            pass

        # Enter a parse tree produced by APPParser#VarField.
        def enterVarField(self, ctx: APPParser.VarFieldContext):
            field = ctx.STRING().getText().strip('"')
            self.fields[self.outer.fieldType] = field
            pass

        # Enter a parse tree produced by APPParser#OptionField.
        def enterOptionField(self, ctx: APPParser.OptionFieldContext):
            field = ctx.STRING().getText()
            self.fields[self.outer.fieldType] = field
            pass

        # Enter a parse tree produced by APPParser#OperatorField.
        def enterOperatorField(self, ctx: APPParser.OperatorFieldContext):
            field = ctx.STRING().getText().strip('"')
            if field == "e ^":
                field = "exp"
            elif field == "10 ^":
                field = "pow10"             
            self.fields[self.outer.fieldType] = field
            pass

        # Enter a parse tree produced by APPParser#IsItTopLevel.
        def enterIsItTopLevel(self, ctx: APPParser.IsItTopLevelContext):
            self.topLevel = self.outer.toBool(ctx.value().getText())
            block = self.outer.Block(self.identifier, self.opcode, self.next, self.parent,
                                     self.inputList, self.fields, self.substacks, self.topLevel)
            self.outer.blocks[self.identifier] = block
            if self.opcode == None:
                raise ValueError("identifier cannot be None")
            if (self.topLevel):
                self.outer.rootNodes.append(self.identifier)
            pass

        # Enter a parse tree produced by APPParser#customBlockInput.
        def enterCustomBlockInput(self, ctx: APPParser.CustomBlockInputContext):
            field = ctx.STRING().getText().strip('"')
            self.fields[self.outer.fieldType] = field
            pass

        # Enter a parse tree produced by APPParser#ProcName.
        def enterProcName(self, ctx: APPParser.ProcNameContext):
            procNm = ctx.value().STRING().getText().strip('"')
            procName = procNm.split(" ")[0]
            self.inputList.append(procName)
            pass

        # Enter a parse tree produced by APPParser#UnMatched.
        def enterUnMatched(self, ctx: APPParser.UnMatchedContext):
            pass

    def getBlockType(self, opcode):
        t = Template(scratchToPython[opcode])
        return t

    def assignInputs(self, params, inputs):
        p = re.compile("^\"?(\\d+(\\.\\d+)?)(?!\\w)\"?$")
        i = 0
        for input in inputs:
            input = self.convertToPy(input)
            m = p.match(input)
            if m:
                input = m.group(1)
            i += 1
            params["i" + str(i)] = input

    def assignFields(self, params, fields):
        f = 0
        for k in fields:
            if k == 'OPERATOR':
                return self.getBlockType(fields[k])
            else:
                f += 1
                params["f" + str(f)] = self.convertToPy(fields[k])
                return None

    def assignSubStack(self, params, subStacks, tabs):
        s = 0
        for sb in subStacks:
            sb = self.convertToPy(sb, tabs)
            s += 1
            params["sb" + str(s)] = sb

    def convertToPy(self, identifier, tabs=0):
        params = {"tbs": tabs*"\t"}

        if identifier == "null":
            return ""

        if identifier not in self.blocks:
            if identifier not in self.varCodeToName:
                return identifier
            return self.varCodeToName[identifier]

        block = self.blocks[identifier]

        blockType = self.getBlockType(block.getOpcode())

        fields = block.getFields()
        inputs = block.getInputList()

        if block.getOpcode() == 'procedures_prototype':
            inputs = [self.convertToPy(i).strip() for i in inputs]
            self.funcAttrs = inputs[:-1]
            inputs = [inputs[-1:][0], ", ".join(inputs[:-1])]

        subStacks = block.getSubstacks()

        self.assignInputs(params, inputs)
        t = self.assignFields(params, fields)
        blockType = t if t != None else blockType
        self.assignSubStack(params, subStacks, tabs + 1)
        if block.getOpcode() == 'procedures_definition':
            tabs += 1

        return blockType.render(**params) + self.convertToPy(block.getNext(), tabs)


def parse(file):
    lexer = APPLexer(FileStream(file))
    stream = CommonTokenStream(lexer)
    parser = APPParser(stream)
    tree = parser.json()

    projectJsonParser = ProjectJsonParser()
    printer = projectJsonParser.PrintPythonCodeListener(projectJsonParser)

    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    str = ''

    for rootNode in projectJsonParser.rootNodes:
        str += projectJsonParser.convertToPy(rootNode)

    return str, projectJsonParser.funcAttrs
