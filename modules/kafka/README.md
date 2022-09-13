To deploy a Kafka in kubernetes, follow the steps below:

1. Install helm

2. Include the helm repo from bitnami `helm repo add bitnami https://charts.bitnami.com/bitnami`

3. Run helm kafka-release `helm install kafka-release bitnami/kafka`