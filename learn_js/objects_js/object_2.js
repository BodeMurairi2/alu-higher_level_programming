#!/usr/bin/node

const my_band = {
    name: "TPOK Jazz",
    nationality: "Congo DRC",
    genre: "Congolese Rumba (Soukous)",
    formed: 1956,
    split: 1993,
    albums: [
        {
            "name": "On Entre OK, On Sort KO",
            "released": 1956
        },
        {
            "name": "Cheri Zozo",
            "released": 1962
        },
        {
            "name": "Ngai Marie Nzoto Ebeba",
            "released": 1965
        },
        {
            "name": "Celine",
            "released": 1969
        },
        {
            "name": "Mado",
            "released": 1969
        }
    ]
}

let band_info = `${my_band.name} from ${my_band.nationality} active from ${my_band.formed} to ${my_band.split} playing ${my_band.genre} genre. The first album is ${my_band.albums[0].name}`;
console.log(band_info);

