package com.example.aqualog.user;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
class LoadUsersDatabase {

  private static final Logger log = LoggerFactory.getLogger(LoadUsersDatabase.class);

  @Bean
  CommandLineRunner initDatabase(UserRepository repository) {

    return args -> {
      log.info("Preloading " + repository.save(new User("Bilbo", "Baggins", "test@example.com")));
      log.info("Preloading " + repository.save(new User("Frodo", "Baggins", "test@example.com")));
    };
  }
}