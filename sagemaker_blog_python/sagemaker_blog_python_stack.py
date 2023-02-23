from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    # aws_iam as iam,
    # aws_sns as sns,
    aws_sagemaker_alpha as sagemaker,

)
from constructs import Construct
import pathlib as path


class SagemakerBlogPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        image = sagemaker.ContainerImage.from_asset("path/to/Dockerfile/directory")
        model_data = sagemaker.ModelData.from_asset("path/to/artifact/file.tar.gz")

        model = sagemaker.Model(self, "PrimaryContainerModel",
                                containers=[sagemaker.ContainerDefinition(
                                    image=image,
                                    model_data=model_data
                                )])

        variant_name = "my-variant"
        endpoint_config = sagemaker.EndpointConfig(self, "EndpointConfig",
                                                   instance_production_variants=[
                                                       sagemaker.InstanceProductionVariantProps(
                                                           model=model,
                                                           variant_name=variant_name
                                                       )
                                                   ]
                                                   )

        endpoint = sagemaker.Endpoint(self, "Endpoint", endpoint_config=endpoint_config)
        production_variant = endpoint.find_instance_production_variant(variant_name)
        instance_count = production_variant.auto_scale_instance_count(
            max_capacity=3
        )
        instance_count.scale_on_invocations("LimitRPS",
                                            max_requests_per_second=30
                                            )
