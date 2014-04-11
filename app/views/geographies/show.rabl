object @geography

node(:type) { "Feature" }

node :geometry do |geog|
  RGeo::GeoJSON.encode(geog.geom)
end

node :properties do |geog|
  { name: geog.name }
end