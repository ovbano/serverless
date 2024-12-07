const AWS = require("aws-sdk");

exports.deleteTask = async (event) => {
    const dynamodb = new AWS.DynamoDB.DocumentClient();
    const {id} = event.pathParameters;

    await dynamodb.delete({
        TableName: "tasksTableVB",
        Key: { id },
    }).promise();
    return {
        status: 200,
        body: JSON.stringify({
            message: "Tarea Eliminada ✔️",
        }),
    };
};