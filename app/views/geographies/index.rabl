object false
node(:type) { "FeatureCollection" }

child @geographies => :features do
  extends 'geographies/show'
end
