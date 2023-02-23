import aws_cdk as core
import aws_cdk.assertions as assertions

from sagemaker_blog_python.sagemaker_blog_python_stack import SagemakerBlogPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sagemaker_blog_python/sagemaker_blog_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SagemakerBlogPythonStack(app, "sagemaker-blog-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
