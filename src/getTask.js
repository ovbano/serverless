const AWS = require("aws-sdk");

exports.getTask = async (event) => {
    const dynamodb = new AWS.DynamoDB.DocumentClient();

    const result = await dynamodb.scan({
        TableName: "tasksTableVB",
    }).promise();
    const tasks = result.Items;
    return {
        status: 200,
        body: {tasks, },
    };
};
