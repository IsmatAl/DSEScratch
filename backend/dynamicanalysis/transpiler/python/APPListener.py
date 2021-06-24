# Generated from APP.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .APPParser import APPParser
else:
    from APPParser import APPParser

# This class defines a complete listener for a parse tree produced by APPParser.
class APPListener(ParseTreeListener):

    # Enter a parse tree produced by APPParser#json.
    def enterJson(self, ctx:APPParser.JsonContext):
        pass

    # Exit a parse tree produced by APPParser#json.
    def exitJson(self, ctx:APPParser.JsonContext):
        pass


    # Enter a parse tree produced by APPParser#obj.
    def enterObj(self, ctx:APPParser.ObjContext):
        pass

    # Exit a parse tree produced by APPParser#obj.
    def exitObj(self, ctx:APPParser.ObjContext):
        pass


    # Enter a parse tree produced by APPParser#ignoredPair.
    def enterIgnoredPair(self, ctx:APPParser.IgnoredPairContext):
        pass

    # Exit a parse tree produced by APPParser#ignoredPair.
    def exitIgnoredPair(self, ctx:APPParser.IgnoredPairContext):
        pass


    # Enter a parse tree produced by APPParser#ProcName.
    def enterProcName(self, ctx:APPParser.ProcNameContext):
        pass

    # Exit a parse tree produced by APPParser#ProcName.
    def exitProcName(self, ctx:APPParser.ProcNameContext):
        pass


    # Enter a parse tree produced by APPParser#ProcArgs.
    def enterProcArgs(self, ctx:APPParser.ProcArgsContext):
        pass

    # Exit a parse tree produced by APPParser#ProcArgs.
    def exitProcArgs(self, ctx:APPParser.ProcArgsContext):
        pass


    # Enter a parse tree produced by APPParser#variables.
    def enterVariables(self, ctx:APPParser.VariablesContext):
        pass

    # Exit a parse tree produced by APPParser#variables.
    def exitVariables(self, ctx:APPParser.VariablesContext):
        pass


    # Enter a parse tree produced by APPParser#VariablePair.
    def enterVariablePair(self, ctx:APPParser.VariablePairContext):
        pass

    # Exit a parse tree produced by APPParser#VariablePair.
    def exitVariablePair(self, ctx:APPParser.VariablePairContext):
        pass


    # Enter a parse tree produced by APPParser#arr.
    def enterArr(self, ctx:APPParser.ArrContext):
        pass

    # Exit a parse tree produced by APPParser#arr.
    def exitArr(self, ctx:APPParser.ArrContext):
        pass


    # Enter a parse tree produced by APPParser#value.
    def enterValue(self, ctx:APPParser.ValueContext):
        pass

    # Exit a parse tree produced by APPParser#value.
    def exitValue(self, ctx:APPParser.ValueContext):
        pass


    # Enter a parse tree produced by APPParser#blocks.
    def enterBlocks(self, ctx:APPParser.BlocksContext):
        pass

    # Exit a parse tree produced by APPParser#blocks.
    def exitBlocks(self, ctx:APPParser.BlocksContext):
        pass


    # Enter a parse tree produced by APPParser#BlockIdentifier.
    def enterBlockIdentifier(self, ctx:APPParser.BlockIdentifierContext):
        pass

    # Exit a parse tree produced by APPParser#BlockIdentifier.
    def exitBlockIdentifier(self, ctx:APPParser.BlockIdentifierContext):
        pass


    # Enter a parse tree produced by APPParser#operation.
    def enterOperation(self, ctx:APPParser.OperationContext):
        pass

    # Exit a parse tree produced by APPParser#operation.
    def exitOperation(self, ctx:APPParser.OperationContext):
        pass


    # Enter a parse tree produced by APPParser#ignorable.
    def enterIgnorable(self, ctx:APPParser.IgnorableContext):
        pass

    # Exit a parse tree produced by APPParser#ignorable.
    def exitIgnorable(self, ctx:APPParser.IgnorableContext):
        pass


    # Enter a parse tree produced by APPParser#NextBlk.
    def enterNextBlk(self, ctx:APPParser.NextBlkContext):
        pass

    # Exit a parse tree produced by APPParser#NextBlk.
    def exitNextBlk(self, ctx:APPParser.NextBlkContext):
        pass


    # Enter a parse tree produced by APPParser#ParentBlk.
    def enterParentBlk(self, ctx:APPParser.ParentBlkContext):
        pass

    # Exit a parse tree produced by APPParser#ParentBlk.
    def exitParentBlk(self, ctx:APPParser.ParentBlkContext):
        pass


    # Enter a parse tree produced by APPParser#InputOfBlk.
    def enterInputOfBlk(self, ctx:APPParser.InputOfBlkContext):
        pass

    # Exit a parse tree produced by APPParser#InputOfBlk.
    def exitInputOfBlk(self, ctx:APPParser.InputOfBlkContext):
        pass


    # Enter a parse tree produced by APPParser#FieldsOfBlk.
    def enterFieldsOfBlk(self, ctx:APPParser.FieldsOfBlkContext):
        pass

    # Exit a parse tree produced by APPParser#FieldsOfBlk.
    def exitFieldsOfBlk(self, ctx:APPParser.FieldsOfBlkContext):
        pass


    # Enter a parse tree produced by APPParser#ShadowOfBlk.
    def enterShadowOfBlk(self, ctx:APPParser.ShadowOfBlkContext):
        pass

    # Exit a parse tree produced by APPParser#ShadowOfBlk.
    def exitShadowOfBlk(self, ctx:APPParser.ShadowOfBlkContext):
        pass


    # Enter a parse tree produced by APPParser#IsItTopLevel.
    def enterIsItTopLevel(self, ctx:APPParser.IsItTopLevelContext):
        pass

    # Exit a parse tree produced by APPParser#IsItTopLevel.
    def exitIsItTopLevel(self, ctx:APPParser.IsItTopLevelContext):
        pass


    # Enter a parse tree produced by APPParser#UnMatched.
    def enterUnMatched(self, ctx:APPParser.UnMatchedContext):
        pass

    # Exit a parse tree produced by APPParser#UnMatched.
    def exitUnMatched(self, ctx:APPParser.UnMatchedContext):
        pass


    # Enter a parse tree produced by APPParser#ValueBlk.
    def enterValueBlk(self, ctx:APPParser.ValueBlkContext):
        pass

    # Exit a parse tree produced by APPParser#ValueBlk.
    def exitValueBlk(self, ctx:APPParser.ValueBlkContext):
        pass


    # Enter a parse tree produced by APPParser#InstructionBlk.
    def enterInstructionBlk(self, ctx:APPParser.InstructionBlkContext):
        pass

    # Exit a parse tree produced by APPParser#InstructionBlk.
    def exitInstructionBlk(self, ctx:APPParser.InstructionBlkContext):
        pass


    # Enter a parse tree produced by APPParser#OpCodeOfBlk.
    def enterOpCodeOfBlk(self, ctx:APPParser.OpCodeOfBlkContext):
        pass

    # Exit a parse tree produced by APPParser#OpCodeOfBlk.
    def exitOpCodeOfBlk(self, ctx:APPParser.OpCodeOfBlkContext):
        pass


    # Enter a parse tree produced by APPParser#ignored.
    def enterIgnored(self, ctx:APPParser.IgnoredContext):
        pass

    # Exit a parse tree produced by APPParser#ignored.
    def exitIgnored(self, ctx:APPParser.IgnoredContext):
        pass


    # Enter a parse tree produced by APPParser#instruction_block.
    def enterInstruction_block(self, ctx:APPParser.Instruction_blockContext):
        pass

    # Exit a parse tree produced by APPParser#instruction_block.
    def exitInstruction_block(self, ctx:APPParser.Instruction_blockContext):
        pass


    # Enter a parse tree produced by APPParser#value_block.
    def enterValue_block(self, ctx:APPParser.Value_blockContext):
        pass

    # Exit a parse tree produced by APPParser#value_block.
    def exitValue_block(self, ctx:APPParser.Value_blockContext):
        pass


    # Enter a parse tree produced by APPParser#fields.
    def enterFields(self, ctx:APPParser.FieldsContext):
        pass

    # Exit a parse tree produced by APPParser#fields.
    def exitFields(self, ctx:APPParser.FieldsContext):
        pass


    # Enter a parse tree produced by APPParser#fieldPair.
    def enterFieldPair(self, ctx:APPParser.FieldPairContext):
        pass

    # Exit a parse tree produced by APPParser#fieldPair.
    def exitFieldPair(self, ctx:APPParser.FieldPairContext):
        pass


    # Enter a parse tree produced by APPParser#field_type.
    def enterField_type(self, ctx:APPParser.Field_typeContext):
        pass

    # Exit a parse tree produced by APPParser#field_type.
    def exitField_type(self, ctx:APPParser.Field_typeContext):
        pass


    # Enter a parse tree produced by APPParser#VarField.
    def enterVarField(self, ctx:APPParser.VarFieldContext):
        pass

    # Exit a parse tree produced by APPParser#VarField.
    def exitVarField(self, ctx:APPParser.VarFieldContext):
        pass


    # Enter a parse tree produced by APPParser#customBlockInput.
    def enterCustomBlockInput(self, ctx:APPParser.CustomBlockInputContext):
        pass

    # Exit a parse tree produced by APPParser#customBlockInput.
    def exitCustomBlockInput(self, ctx:APPParser.CustomBlockInputContext):
        pass


    # Enter a parse tree produced by APPParser#OptionField.
    def enterOptionField(self, ctx:APPParser.OptionFieldContext):
        pass

    # Exit a parse tree produced by APPParser#OptionField.
    def exitOptionField(self, ctx:APPParser.OptionFieldContext):
        pass


    # Enter a parse tree produced by APPParser#OperatorField.
    def enterOperatorField(self, ctx:APPParser.OperatorFieldContext):
        pass

    # Exit a parse tree produced by APPParser#OperatorField.
    def exitOperatorField(self, ctx:APPParser.OperatorFieldContext):
        pass


    # Enter a parse tree produced by APPParser#inputs.
    def enterInputs(self, ctx:APPParser.InputsContext):
        pass

    # Exit a parse tree produced by APPParser#inputs.
    def exitInputs(self, ctx:APPParser.InputsContext):
        pass


    # Enter a parse tree produced by APPParser#input_type.
    def enterInput_type(self, ctx:APPParser.Input_typeContext):
        pass

    # Exit a parse tree produced by APPParser#input_type.
    def exitInput_type(self, ctx:APPParser.Input_typeContext):
        pass


    # Enter a parse tree produced by APPParser#inputVals.
    def enterInputVals(self, ctx:APPParser.InputValsContext):
        pass

    # Exit a parse tree produced by APPParser#inputVals.
    def exitInputVals(self, ctx:APPParser.InputValsContext):
        pass


    # Enter a parse tree produced by APPParser#LiteralInput.
    def enterLiteralInput(self, ctx:APPParser.LiteralInputContext):
        pass

    # Exit a parse tree produced by APPParser#LiteralInput.
    def exitLiteralInput(self, ctx:APPParser.LiteralInputContext):
        pass


    # Enter a parse tree produced by APPParser#ValInput.
    def enterValInput(self, ctx:APPParser.ValInputContext):
        pass

    # Exit a parse tree produced by APPParser#ValInput.
    def exitValInput(self, ctx:APPParser.ValInputContext):
        pass


    # Enter a parse tree produced by APPParser#InstrucInput.
    def enterInstrucInput(self, ctx:APPParser.InstrucInputContext):
        pass

    # Exit a parse tree produced by APPParser#InstrucInput.
    def exitInstrucInput(self, ctx:APPParser.InstrucInputContext):
        pass


    # Enter a parse tree produced by APPParser#app.
    def enterApp(self, ctx:APPParser.AppContext):
        pass

    # Exit a parse tree produced by APPParser#app.
    def exitApp(self, ctx:APPParser.AppContext):
        pass



del APPParser