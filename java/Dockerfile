FROM openjdk:17-jdk

WORKDIR /analyzer

COPY /api/target/api-1.0-SNAPSHOT.jar /analyzer/app.jar

ENTRYPOINT ["java", "-jar", "/analyzer/app.jar"]
