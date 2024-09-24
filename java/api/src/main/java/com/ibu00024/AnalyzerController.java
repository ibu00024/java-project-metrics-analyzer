package com.ibu00024;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

@RestController
public class AnalyzerController {

    @PostMapping("/analyze")
    public String analyzeRepo(@RequestParam("repo_path") String repoPath) throws IOException, InterruptedException {
        InputStream jarStream = getClass().getClassLoader().getResourceAsStream("CodeMetricAnalyzer.jar");

        Path tempJarPath = Files.createTempFile("CodeMetricAnalyzer", ".jar");
        Files.copy(jarStream, tempJarPath, StandardCopyOption.REPLACE_EXISTING);

        Process process = new ProcessBuilder("java", "-jar", tempJarPath.toString(), repoPath).start();
        process.waitFor();

        String output = new String(process.getInputStream().readAllBytes());
        String errorOutput = new String(process.getErrorStream().readAllBytes());

        if (!errorOutput.isEmpty()) {
            return "Error: " + errorOutput;
        }

        return output;
    }
}
