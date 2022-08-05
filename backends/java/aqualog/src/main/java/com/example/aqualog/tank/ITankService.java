package com.example.aqualog.tank;

interface ITankService {

    Tank findTankById(Long id);
    Tank addTank(Tank newTank);
    Tank upsertTank(Tank newTank, Long id);
    void deleteTank(Long id);

}
