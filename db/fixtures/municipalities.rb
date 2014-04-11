require 'csv'

def municipalities
  munis = File.new(Rails.root + 'db/fixtures/geometries/municipalities/mf_munis.csv')
  
  CSV.parse(munis, headers: true).map {|row|
    row.headers.zip([row['muni_id'], row['name'], row['geom']])
  }.map {|obj| Hash[*obj.flatten]}
end