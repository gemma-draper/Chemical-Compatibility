# Chemical-Compatibility

A database for checking chemical compatibility with sample environment materials at ISIS Pulsed Neutron and Muon Source.

## Background

Experiments at ISIS have grown increasingly complex in recent years; one facet of this is the complexity of the chemical systems used. These experiments frequently utilise high temperatures and pressures, and ensuring the safety of experiments is a key concern. It is therefore vital for us to consider potential interactions between the chemicals used and the sample environment equipment we provide. A thorough understanding of these interactions enables engineers and technicians to design or select suitable equipment for a given experiment. 

Equipment we wish to consider includes:
- Gas handling panels
    - Stainless steel tubing (SS-316)
    - Pressure relief valves (SS-316, various elastomers)
    - Pressure transducers
    - Valves (SS-316, elastomers)
- Sample containers
    - Sample cells (various metals, alloys, glasses and plastics)
    - Container seals (various metals, elastomers)
- Vacuum pumps
- Gas cylinder regulators
- Pressure generators

In 2019, the ISIS Sample Environment Group created a simple spreadsheet to summarise the available literature for compatibility of the materials with various chemicals at room temperature. You can see a snapshot of this spreadsheet below. 

![A snapshot of the chemical compatibility spreadsheet.](https://user-images.githubusercontent.com/84348138/135100089-1d33d611-8503-48ec-af92-4b08f8071123.png)

## Motivation
Alongside ensuring the safety of experiments, covered above, cost reduction and environmental sustainability are also major project motivations. Sample environment equipment is often designed with a finite lifetime, but the conditions of use can drastically alter its service life. For example, a sample cell designed to be scrapped after a single use could in reality be  used several times depending on its use conditions. Since sample cells are often made of exotic materials, they can be costly to manufacture both in terms of price and energy. If, by better understanding the beahviour of these materials under different temperature, pressure and chemical conditions, we could extend the lifetime of sample environment equipment we could realise both cost and environmental benefits. 

## Project aims

- Migrate data to a SQL database.
- Expand to include temperature data.
- Deploy API.
- Browser-based search function.
