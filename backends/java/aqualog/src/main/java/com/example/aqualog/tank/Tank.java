package com.example.aqualog.tank;

import java.util.Date;
import java.util.Objects;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import com.example.aqualog.user.User;

@Entity
@Table(name="tanks")
public class Tank {

    @Column(name="`id`")
    private @Id @GeneratedValue(strategy = GenerationType.IDENTITY) Long id;

    @Column(name="`name`")
    private String name;

    @Column(name="`capacity`")
    private Long capacity;

    @Column(name="`unit_type`")
    private UnitType unitType;

    @Column(name="`water_type`")
    private WaterType waterType;

    @ManyToOne
    @JoinColumn(name = "user_id", referencedColumnName = "id")
    private User user;

    @CreationTimestamp
    @Column(name="`created_at`")
    private Date createdAt;

    @UpdateTimestamp
    @Column(name="`updated_at`")
    private Date updatedAt;

    // getters
    public Long getId(){
        return this.id;
    }

    public String getName(){
        return this.name;
    }

    public Long getCapacity(){
        return this.capacity;
    }

    public WaterType getWaterType(){
        return this.waterType;
    }

    public UnitType getUnitType(){
        return this.unitType;
    }

    public Date getCreatedAt(){
        return this.createdAt;
    }

    public Date getUpdatedAt(){
        return this.updatedAt;
    }

    // setters
    public void setId(Long id){
        this.id = id;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setCapacity(Long capacity){
        this.capacity = capacity;
    }

    public void setWaterType(WaterType waterType){
        this.waterType = waterType;
    }

    public void setUnitType(UnitType unitType){
        this.unitType = unitType;
    }

    public void setUpdatedAt(Date updatedAt){
        this.updatedAt = updatedAt;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Tank tank = (Tank) o;
        return id == tank.id &&
                capacity == tank.capacity &&
                Objects.equals(name, tank.name) &&
                Objects.equals(waterType, tank.waterType) &&
                Objects.equals(unitType, tank.unitType) &&
                Objects.equals(user, tank.user); //&&
                // Objects.equals(createdAt, user.createdAt) &&
                // Objects.equals(updatedAt, user.updatedAt);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.id, this.name, this.capacity, this.user.getEmail());
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("User{");
        sb.append("id=").append(this.id);
        sb.append(", name='").append(this.name).append('\'');
        sb.append(", capacity='").append(this.capacity).append('\'');
        sb.append(", waterType='").append(this.waterType).append('\'');
        sb.append(", unitType='").append(this.unitType).append('\'');
        sb.append(", createdAt='").append(this.createdAt).append('\'');
        sb.append('}');
        return sb.toString();
    }
}
