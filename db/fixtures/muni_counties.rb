require 'csv'

def muni_counties
  CSV.foreach('db/fixtures/relations/muni_counties.csv', headers: true) do |row|
    municipality_id = row['municipality_id']
    county_id = row['county_id']

    Municipality.find(municipality_id).update_attribute(:county_id, county_id)
  end
end
