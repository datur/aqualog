package com.example.aqualog;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AquaLogController {

	@GetMapping("/")
	public String index() {
		return "Greetings from Spring Boot!";
	}

}