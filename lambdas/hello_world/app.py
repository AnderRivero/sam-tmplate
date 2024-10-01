from lambdas.layers.bodyResponse import bodyresponse


def lambda_handler(event, context):

    return bodyresponse(200, "Hello World Ander")
