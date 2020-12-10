#!/usr/bin/env python3

from aws_cdk import core

from codepipeline.codepipeline_stack import CodepipelineStack
from codepipeline.pipeline_stack import PiplelineStack

app = core.App()
CodepipelineStack(app, "codepipeline")
PiplelineStack(app, 'PipelineStack', env={
    'account': '528811707541',
    'region': 'us-west-2'
})

app.synth()
