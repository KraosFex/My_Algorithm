function inventarioDeLaGranja(vacas, pollos){
    let stringVacas = String(vacas);
    while(stringVacas.length < 3){
        stringVacas = "0" + stringVacas
    }
    console.log(`${stringVacas} Vacas`);

    let stringPollos = String(pollos);
    while (stringPollos.length < 3) {
        stringPollos = "0" + stringPollos;
    }
    console.log(`${stringPollos} Pollos`);
}

inventarioDeLaGranja(7, 11);