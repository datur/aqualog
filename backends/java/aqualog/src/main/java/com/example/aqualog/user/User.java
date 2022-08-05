package com.example.aqualog.user;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.util.Date;
import java.util.Objects;

@Entity
@Table(name="users")
public class User {

    @Column(name="`id`")
    private @Id @GeneratedValue(strategy = GenerationType.IDENTITY) Long id;

    @Column(name="`first_name`")
    private String firstName;

    @Column(name="`last_name`")
    private String lastName;

    @Column(name="`email`", unique=true)
    private String email;

    @CreationTimestamp
    @Column(name="`created_at`")
    private Date createdAt;

    @UpdateTimestamp
    @Column(name="`updated_at`")
    private Date updatedAt;

    public User(){
    }

    public User(String firstName, String lastName, String email){
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
    }

    // Getters
    public Long getId(){
        return this.id;
    }

    public String getFirstName(){
        return this.firstName;
    }

    public String getLastName(){
        return this.lastName;
    }

    public String getEmail(){
        return this.email;
    }

    public Date getCreatedAt(){
        return this.createdAt;
    }

    public Date getUpdatedAt(){
        return this.updatedAt;
    }

    // Setters
    public void setId(Long id){
        this.id = id;
    }

    public void setFirstName(String firstName){
        this.firstName = firstName;
    }

    public void setLastName(String lastName){
        this.lastName = lastName;
    }

    public void setEmail(String email){
        this.email = email;
    }

    public void setUpdatedAt(Date updatedAt){
        this.updatedAt = updatedAt;
    }


    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return id == user.id &&
                Objects.equals(firstName, user.firstName) &&
                Objects.equals(lastName, user.lastName) &&
                Objects.equals(email, user.email); //&&
                // Objects.equals(createdAt, user.createdAt) &&
                // Objects.equals(updatedAt, user.updatedAt);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.id, this.firstName, this.lastName, this.email);
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("User{");
        sb.append("id=").append(this.id);
        sb.append(", firstName='").append(this.firstName).append('\'');
        sb.append(", lastName='").append(this.lastName).append('\'');
        sb.append(", email='").append(this.email).append('\'');
        sb.append(", createdAt='").append(this.createdAt).append('\'');
        sb.append('}');
        return sb.toString();
    }
}
