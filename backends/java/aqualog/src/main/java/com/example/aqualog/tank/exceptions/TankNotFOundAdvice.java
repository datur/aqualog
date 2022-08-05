package com.example.aqualog.tank.exceptions;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;

@ControllerAdvice
class TankNotFoundAdvice {

  @ResponseBody
  @ExceptionHandler(TankNotFoundException.class)
  @ResponseStatus(HttpStatus.NOT_FOUND)
  String TankNotFoundHandler(TankNotFoundException ex) {
    return ex.getMessage();
  }
}