def subregions
  helpers = [{id: 1, abbr: 'ICC',   name: "Inner Core Committee"},
             {id: 2, abbr: 'MAGIC', name: "Minuteman Advisory Group Interlocal Coordination"},
             {id: 3, abbr: 'MWRC',  name: "MetroWest Regional Collaborative"},
             {id: 4, abbr: 'NSTF',  name: "North Shore Task Force"},
             {id: 5, abbr: 'NSPC',  name: "North Suburban Planning Council"},
             {id: 6, abbr: 'SSC',   name: "South Shore Coalition"},
             {id: 7, abbr: 'SWAP',  name: "South West Advisory Planning Committee"},
             {id: 8, abbr: 'TRIC',  name: "Three Rivers Interlocal Council"}]

  subregions = File.new(Rails.root + 'db/fixtures/geometries/subregions/subregions.csv')

  CSV.parse(subregions, headers: true).map {|row|
    helper = helpers.shift
    row.headers.push('abbr').zip([row['id'],
                                  row['muni_id'],
                                  helper[:name],
                                  row['geom'],
                                  helper[:abbr]
                                 ])
  }.map {|obj| Hash[*obj.flatten]}

end