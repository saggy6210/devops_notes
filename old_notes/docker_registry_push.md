Build and Push image into docker registry:

CALL gradlew clean build eclipse -PbuildEnv=az_tag
CALL docker build -t docker_registry_url/image_name:version .
CALL docker login docker_registry_url -u mdspstkacs -p PASSWORD
CALL docker push docker_registry_url/image_name:version
