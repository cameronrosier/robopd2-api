# RoboPD2 API
A REST Api written in Python using FASTAPI and Uvicorn. This API is designed to be used with both the RoboPD2 Twitch Bot and the RoboPD2 Character Planner.

## Installation
This application is meant to be deployed to a kubernetes cluster. The following steps will guide you through the process of deploying the application to a kubernetes cluster using helm.

```bash
helm install robopd2-api ./charts --create-namespace --set secret.robopd2MongoHost=<MONGO_HOST> --set secret.robopd2MongoPass=<MONGO_PASS> --set secret.robopd2MongoPort=:<MONGO_PORT> --set secret.robopd2MongoUser=<MONGO_USER> -n robopd2
```

This will create a deployment of the robopd2-api application as well as a service and ingress to expose the application to the internet.