package com.example.aqualog.user;

import org.springframework.stereotype.Service;
import com.example.aqualog.user.exceptions.UserNotFoundException;

@Service
public class UserService implements IUserService {

    private final UserRepository _repository;

    UserService(UserRepository repository){
        this._repository = repository;
    }

    public User findUserById(Long id) {
        return _repository.findById(id).orElseThrow(() -> new UserNotFoundException(id));
    }

    public User addUser(User newUser){
        return _repository.save(newUser);
    }

    public User upsertUser(User newUser, Long id){
        return _repository.findById(id)
            .map(user -> {
                user.setFirstName(newUser.getFirstName() != null ? newUser.getFirstName() : user.getFirstName());
                user.setLastName(newUser.getLastName() != null ? newUser.getLastName() : user.getLastName());
                user.setEmail(newUser.getEmail() != null ? newUser.getEmail() : user.getEmail());
                return _repository.save(user);
            })
            .orElseGet(() -> {
                newUser.setId(id);
                return _repository.save(newUser);
            });
    }

    public void deleteUser(Long id){
        var result = findUserById(id);

		if (result != null){
			_repository.deleteById(id);
		}
    }

}