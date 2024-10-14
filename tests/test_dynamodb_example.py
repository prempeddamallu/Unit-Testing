import boto3
from src.boto3_example import DynamodBExample
from moto import mock_aws
from botocore.exceptions import ClientError

@mock_aws
def test_create_dynamo_table():
    # Arrange
    dynamo_example = DynamodBExample()

    # Act``
    dynamo_example.create_movies_table()

    # Assert
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Movies')
    assert table.table_status == 'ACTIVE'

@mock_aws
def test_add_dynamo_record_table():
    # Arrange
    dynamo_example = DynamodBExample()
    dynamo_example.create_movies_table()

    # Sample item to insert
    item = {
        'year': 2024,
        'title': 'Test Movie',
        'info': {'plot': 'Nothing happens at all.'}
    }

    # Act
    dynamo_example.add_dynamo_record('Movies', item)

    # Assert
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Movies')
    response = table.get_item(Key={'year': 2024, 'title': 'Test Movie'})
    assert 'Item' in response
    assert response['Item']['title'] == 'Test Movie'
    assert response['Item']['year'] == 2024

@mock_aws
def test_add_dynamo_record_table_failure():
    # Arrange
    dynamo_example = DynamodBExample()

    # Act & Assert
    try:
        # Try to add a record to a non-existent table
        item = {
            'year': 2024,
            'title': 'Test Movie',
            'info': {'plot': 'Nothing happens at all.'}
        }
        dynamo_example.add_dynamo_record('NonExistentTable', item)
    except ClientError as e:
        assert e.response['Error']['Code'] == 'ResourceNotFoundException'

