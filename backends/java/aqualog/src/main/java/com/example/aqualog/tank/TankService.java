package com.example.aqualog.tank;

import org.springframework.stereotype.Service;

import com.example.aqualog.tank.exceptions.TankNotFoundException;

@Service
public class TankService implements ITankService {

    private final TankRepository _repository;

    TankService(TankRepository repository){
        this._repository = repository;
    }

    public Tank findTankById(Long id){
        return _repository.findById(id).orElseThrow(() -> new TankNotFoundException(id));
    }

    public Tank addTank(Tank newTank){
        return _repository.save(newTank);
    }

    public Tank upsertTank(Tank newTank, Long id){
        return _repository.findById(id)
            .map(tank -> {
                tank.setName(newTank.getName() != null ? newTank.getName() : tank.getName());
                tank.setCapacity(newTank.getCapacity() != null ? newTank.getCapacity() : tank.getCapacity());
                tank.setUnitType(newTank.getUnitType() != null ? newTank.getUnitType() : tank.getUnitType());
                tank.setWaterType(newTank.getWaterType() != null ? newTank.getWaterType() : tank.getWaterType());
                return _repository.save(tank);
            })
            .orElseGet(() -> {
                newTank.setId(id);
                return _repository.save(newTank);
            });
    }

    public void deleteTank(Long id){
        var result = findTankById(id);

		if (result != null){
			_repository.deleteById(id);
		}
    }

}
