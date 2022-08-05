package com.example.aqualog.tank.exceptions;

public class TankNotFoundException extends RuntimeException {
    public TankNotFoundException(Long id) {
      super("Could not find tank with id: " + id);
    }
  }