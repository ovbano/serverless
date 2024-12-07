const { v4 } = require("uuid");
const AWS = require("aws-sdk");

exports.addTask = async (event) => {
  const dynamodb = new AWS.DynamoDB.DocumentClient();
  const { title, description } = JSON.parse(event.body);
  const createAT = new Date();
  const id = v4();

  const newTask = {
    id,
    title,
    description,
    createAT,
    done: true,
  };
  await dynamodb
    .put({
      TableName: "tasksTableVB",
      Item: newTask,
    })
    .promise();
  return {
    status: 200,
    body: JSON.stringify(newTask),
  };
};