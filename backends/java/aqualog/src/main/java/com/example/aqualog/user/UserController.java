package com.example.aqualog.user;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.aqualog.user.exceptions.UserNotFoundException;


@RestController
public class UserController {

	private final UserService _userService;

	UserController(UserService userService) {
		this._userService = userService;
	  }

    @GetMapping("/user/{id}")
	public User getUser(@PathVariable Long id) {
		try {
			var result = _userService.findUserById(id);
			return result;

		} catch (Exception e) {
			throw new UserNotFoundException(id);
		}
	}

	@PostMapping("/user")
	public User newUser(@RequestBody User newUser){

		return _userService.addUser(newUser);

	}

	@PutMapping("/user/{id}")
    public User replaceEmployee(@RequestBody User newUser, @PathVariable Long id) {

    	return _userService.upsertUser(newUser, id);

	}

	@DeleteMapping("/user/{id}")
	void deleteEmployee(@PathVariable Long id) {

		_userService.deleteUser(id);

	}
}
