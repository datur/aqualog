package com.example.aqualog.reading;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Reading {

    @Column(name="`id`")
    private @Id @GeneratedValue(strategy = GenerationType.IDENTITY) Long id;

    @Column(name="`ph`")
    private float ph;

    @Column(name="`ammonia`")
    private float ammonia;

    @Column(name="`nitrite`")
    private float nitrite;

    @Column(name="`nitrate`")
    private float nitrate;

    @Column(name="`gh`")
    private int gh;

    @Column(name="`kh`")
    private int kh;

    @Column(name="`specific_gravity`")
    private float specificGravity;

    @Column(name="`alkalinity`")
    private int alkalinity;

    @Column(name="`phosphate`")
    private float phosphate;

    @Column(name="`calcium`")
    private int calcium;

    @Column(name="`magnesium`")
    private int magnesium;

    @Column(name="`iodine`")
    private float iodine;

    @Column(name="`strontium`")
    private int strontium;

    @Column(name="`silicate`")
    private float silicate;

    // getters and setters

    public Long getId() {
        return this.id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public float getPh() {
        return this.ph;
    }

    public void setPh(float ph) {
        this.ph = ph;
    }

    public float getAmmonia() {
        return this.ammonia;
    }

    public void setAmmonia(float ammonia) {
        this.ammonia = ammonia;
    }

    public float getNitrite() {
        return this.nitrite;
    }

    public void setNitrite(float nitrite) {
        this.nitrite = nitrite;
    }

    public float getNitrate() {
        return this.nitrate;
    }

    public void setNitrate(float nitrate) {
        this.nitrate = nitrate;
    }

    public int getGh() {
        return this.gh;
    }

    public void setGh(int gh) {
        this.gh = gh;
    }

    public int getKh() {
        return this.kh;
    }

    public void setKh(int kh) {
        this.kh = kh;
    }

    public float getSpecificGravity() {
        return this.specificGravity;
    }

    public void setSpecificGravity(float specificGravity) {
        this.specificGravity = specificGravity;
    }

    public int getAlkalinity() {
        return this.alkalinity;
    }

    public void setAlkalinity(int alkalinity) {
        this.alkalinity = alkalinity;
    }

    public float getPhosphate() {
        return this.phosphate;
    }

    public void setPhosphate(float phosphate) {
        this.phosphate = phosphate;
    }

    public int getCalcium() {
        return this.calcium;
    }

    public void setCalcium(int calcium) {
        this.calcium = calcium;
    }

    public int getMagnesium() {
        return this.magnesium;
    }

    public void setMagnesium(int magnesium) {
        this.magnesium = magnesium;
    }

    public float getIodine() {
        return this.iodine;
    }

    public void setIodine(float iodine) {
        this.iodine = iodine;
    }

    public int getStrontium() {
        return this.strontium;
    }

    public void setStrontium(int strontium) {
        this.strontium = strontium;
    }

    public float getSilicate() {
        return this.silicate;
    }

    public void setSilicate(float silicate) {
        this.silicate = silicate;
    }


}
