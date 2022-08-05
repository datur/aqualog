package com.example.aqualog.user;

interface IUserService {

    User findUserById(Long id);
    User addUser(User newUser);
    User upsertUser(User newUser, Long id);
    void deleteUser(Long id);

}
