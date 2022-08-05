package com.example.aqualog.tank;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.aqualog.tank.exceptions.TankNotFoundException;

@RestController
public class TankController {

    private final TankService _tankService;

    TankController(TankService tankService){
        this._tankService = tankService;
    }

    @GetMapping("/tanks/{id}")
	public Tank getUser(@PathVariable Long id) {
		try {
			var result = _tankService.findTankById(id);
			return result;

		} catch (Exception e) {
			throw new TankNotFoundException(id);
		}
	}

    @PostMapping("/tanks")
	public Tank newUser(@RequestBody Tank newTank){

		return _tankService.addTank(newTank);

	}

	@PutMapping("/tanks/{id}")
    public Tank replaceEmployee(@RequestBody Tank newTank, @PathVariable Long id) {

    	return _tankService.upsertTank(newTank, id);

	}

	@DeleteMapping("/tanks/{id}")
	void deleteEmployee(@PathVariable Long id) {

		_tankService.deleteTank(id);

	}

}
